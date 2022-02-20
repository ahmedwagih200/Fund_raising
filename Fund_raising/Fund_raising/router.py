from myapi.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('project', ProjectList)
router.register('category', CategoryViewset)
router.register('pics', PicsViewset)
router.register('comments', CommentsViewset)
# router.register('tags',TagsViewset)
router.register('reports', ReportsViewset)
router.register('rates', RatesViewset)
router.register('donations', DonationsViewset)
router.register('ReportComments', ReportComments_Viewset)
