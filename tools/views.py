from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .models import Tools, Issues
from .forms import issueForm, MyForm
from django.urls import reverse
from django.forms import formset_factory

def index(request):
    context = {}
    return render(request, 'tools/index.html', context)

def on_stock(request):
    tools =Tools.objects.all()
    context ={'tools':tools}
    return render(request, 'tools/on_stock.html', context)

def all_issues(request):
    issues=Issues.objects.all()
    context={'issues':issues}
    return render(request, 'tools/all_issues.html', context)

def issue(request):

    if request.method=='POST':
        form=issueForm(request.POST)


        if form.is_valid():
            q = Tools.objects.get(name=form.cleaned_data['tool_name'])
            q.qty = q.qty-form.cleaned_data['issue_qty']
            q.save()
            i = Issues(name=form.cleaned_data['tool_name'],
                       qty=form.cleaned_data['issue_qty'])
            i.save()

            return HttpResponseRedirect(reverse('thanks'))


    else:

        form = issueForm()

        #form=issueFormset()

    context = {'form' : form}
    return render(request, 'tools/issue.html', context)

def tool_det(request, tool_name):
    try:
        tool=Tools.objects.get(name=tool_name)
    except Tools.DoesNotExist:
        raise Http404('no such tool')

    context={'tool':tool}
    return render(request, 'tools/tool_det.html', context)

def thanks(request):
    request.GET=1
    info=[request.GET]
    context= {'info':info}

    return render(request, 'tools/thanks.html', context)

def test1(request):
    text='test 1'
    context={'text':text}
    return render(request, 'tools/test.html', context)

def test2(request):
    text='test 2'
    info=[request.GET.get('id','')]
    context={'text':info}

    return render(request, 'tools/test.html', context)


def myview(request):
    e='ee'

    if request.method == 'POST':

        form = MyForm(request.POST,
                      extra=request.POST.get('extra_field_count'),
                      validate=True)
        e=['POST', request.POST]

        if form.is_valid():
            e=['VALID', request.POST]
        #return HttpResponseRedirect(reverse('thanks'))
    else:
        #form = MyForm()

        form = MyForm(request.GET,
                      extra=request.GET.get('extra_field_count'),
                      validate=False)

        e=['GET', request.GET]
    return render(request, 'tools/myview.html', { 'form': form, 'e':e })
