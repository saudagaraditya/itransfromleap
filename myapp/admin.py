from django.contrib import admin
from .models import Question,Option,Response
from django.db.models import Sum


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_total_score','question','option')  # Add 'get_total_score' to list_display

    def get_total_score(self, obj):
        # Retrieve the total score for each user by aggregating the scores of distinct responses
        total_score = Response.objects.filter(user=obj.user).aggregate(total_score=Sum('option__marks'))['total_score']
        return total_score if total_score is not None else 0
    get_total_score.short_description = 'Total Score'  # Set the column header name


admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Response, ResponseAdmin)


