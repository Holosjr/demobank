from . models import Branch,Sbranch
def menu_links(request):
    links=Branch.objects.all()
    links1=Sbranch.objects.all()
    return dict(links=links,links1=links1)