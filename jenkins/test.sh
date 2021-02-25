cd application/expenditure_service
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock
python3 -m pytest --cov=application --cov-report xml 
cd ..

cd report_aggregate_service
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock
python3 -m pytest --cov=application --cov-report xml 
cd ..


cd report_UI
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock
python3 -m pytest --cov=application --cov-report xml 
cd ..


cd revenue_service
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock
python3 -m pytest --cov=application --cov-report xml 
cd ..