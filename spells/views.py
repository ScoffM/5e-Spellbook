from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Spell


def all_spells(request):
    spells = Spell.objects
    return render(request, 'spells/all_spells.html', {'spells': spells})


def detail(request, spell_id):
    detail_spell = get_object_or_404(Spell, pk=spell_id)
    return render(request, 'spells/details.html', {'spell': detail_spell})
