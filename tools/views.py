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

            #url=reverse('thanks', kwargs={'p':1})
            url=reverse('thanks', args=(1,))
            return HttpResponseRedirect(url)


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

    info=[]
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
        e=['POST', request.POST] #TEST - wyświetlanie odpowiedzi

        if form.is_valid():

            data=form.cleaned_data
            data.pop('extra_field_count')
            data.pop('validate')
            data=list(data.values())

            # creating dict from data (tool name:qty) - to be rewritten
            l=[e for e in data if type(e)==str]
            q=[e for e in data if type(e)==int]

            d={}
            for e in :
                d[e]=0
            for e,e1 in zip(l,q):
                temp=d[e]
                d[e]=temp+e1


            # making changes in database
            for key in d:

                q = Tools.objects.get(name=key)
                q.qty = q.qty-d[key]
                q.save()
                i = Issues(name=key,
                           qty=d[key])
                i.save()



            #return render(request, 'tools/myview.html',
            #    { 'form': form, 'e':d})

            return HttpResponseRedirect(reverse('thanks'))
        else:
            return render(request, 'tools/myview.html',
                { 'form': form, 'e':e })

    else:
        #form = MyForm()

        form = MyForm(request.GET,
                      extra=request.GET.get('extra_field_count'),
                      validate=False)

        e=['GET', request.GET]
    return render(request, 'tools/myview.html', { 'form': form, 'e':e })
