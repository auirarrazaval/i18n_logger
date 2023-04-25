from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import i18nLog
from .serializers import i18nLogSerializer
from flatten_json import unflatten


class i18nLogViewSet(viewsets.GenericViewSet):
    queryset = i18nLog.objects.all()
    serializer_class = i18nLogSerializer

    def get_queryset(self):
        if self.action == "generate":
            return i18nLog.objects.filter(locale=self.request.query_params["locale"])
        return i18nLog.objects.get_or_create(
            key=self.request.data["key"],
            locale=self.request.data["locale"],
        )

    def get_serializer_class(self):
        return i18nLogSerializer

    @action(detail=False, methods=["post"])
    def log(self, request):
        log, created = self.get_queryset()
        if created:
            log.save()
        hit = request.data["hit"] or False
        if hit:
            log.hits += 1
            log.value = request.data["value"]
        else:
            log.misses += 1

        log.save()

        return Response({"status": "success", "log": self.get_serializer(log).data})

    @action(
        detail=False,
        methods=["get"],
    )
    def generate(self, request):
        locale = request.query_params.get("locale", None)
        clean = request.query_params.get("clean", False) == "true"
        logs = self.get_queryset()
        if clean:
            logs = logs.filter(~Q(key__contains=" "))
        print(logs)
        logs_flat = {key: value for (key, value) in logs.values_list("key", "value")}
        flat = request.query_params.get("flat", False) == "true"
        if flat:
            return Response({"status": "success", f"{locale}.json": logs_flat})
        logs_unflattened = unflatten(logs_flat, ".")
        return Response({"status": "success", f"{locale}.json": logs_unflattened})
