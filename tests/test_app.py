import unittest
from app import app


class TaskApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")

    def test_create_task(self):
        response = self.client.post("/api/tasks", json={"title": "Write pipeline"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["title"], "Write pipeline")

    def test_reject_empty_title(self):
        response = self.client.post("/api/tasks", json={"title": " "})
        self.assertEqual(response.status_code, 400)

    def test_update_missing_task(self):
        response = self.client.patch("/api/tasks/99999", json={"completed": True})
        self.assertEqual(response.status_code, 404)

    def test_delete_missing_task(self):
        response = self.client.delete("/api/tasks/99999")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
