from about.models import About, SocialMedia, Store
from order.models import OrderItem, WishList
from product.models import Category


def header_and_footer(request):

    context = {
        'context_categories': Category.objects.all().order_by('order') if Category.objects.all() else [],
        'store': Store.objects.first(),
        'footer_about': About.objects.first(),
        'social': SocialMedia.objects.first(),
    }
    if request.user.is_authenticated:
        context.update({
            'basket_order_count': OrderItem.objects.filter(user=request.user, status=0).count() or 0,
            'wish_list_count': WishList.objects.filter(user=request.user).first().product.count() if WishList.objects.filter(user=request.user).first() else 0
            })

    return context