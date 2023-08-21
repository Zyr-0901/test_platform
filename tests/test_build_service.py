from service.build_service import BuildService


class TestBuildService:

    def setup_class(self):
        self.build = BuildService()

    def test_get(self):
        self.build.get(1)

    def test_all(self):
        self.build.list()

    def test_create(self):
        build_result = self.build.create(3)
        assert build_result

    def test_delete(self):
        result = self.build.delete(1)
        assert result



