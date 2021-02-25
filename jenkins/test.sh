cd application/expenditure_service/tests
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock
python3 -m pytest --cov=expenditure_service --cov-report 
cd .. /..

cd report_aggregate_service/tests
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock
python3 -m pytest --cov=report_aggregate_service --cov-report 
cd ../..


cd report_UI/tests
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock
python3 -m pytest --cov=report_UI --cov-report 
cd ../..


cd revenue_service/tests
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock
python3 -m pytest --cov=revenue_service --cov-report  
cd ../../..