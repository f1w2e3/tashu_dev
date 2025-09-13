# Create your tests here

from django.test import TestCase
from django.utils import timezone
from .models import Prediction

class PredictionModelTest(TestCase):
    def test_prediction_creation(self):
        """Prediction 객체가 정상적으로 생성되는지 확인"""
        prediction = Prediction.objects.create(
            station_id=1,
            predicted_bikes=10,
            predicted_time=timezone.now()
        )
        self.assertEqual(prediction.station_id, 1)
        self.assertEqual(prediction.predicted_bikes, 10)
        self.assertIsNotNone(prediction.predicted_time)
