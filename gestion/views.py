from django.shortcuts import render
from gestion.models import SubUnit, Unit
from django.http import Http404


def main(request):
    """
    Front page.
    """
    return render(request, "main.html", context={"units": Unit.objects.all()})


def unit(request, order: int):
    """
    Section view
    """

    # Check if there's an unit with this order (i.e. 2, 3, etc)
    if this_unit := Unit.objects.filter(order=order).first():
        return render(
            request,
            "unit.html",
            context={
                "this_unit": this_unit,
                "units": Unit.objects.all(),
                "subunits": SubUnit.objects.filter(parent=this_unit),
            },
        )
    raise Http404()
