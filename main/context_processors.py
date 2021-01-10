from .models import Category

def list_all_categories(request):
    return {'all_categories': Category.objects.all()
            }
