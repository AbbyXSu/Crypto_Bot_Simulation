cd application/expenditure_service
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock
python3 -m pytest --cov=expenditure_service 
cd ../.. 

cd application/report_aggregate_service
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock
python3 -m pytest --cov=report_aggregate_service 
cd ../..


cd application/report_UI
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock
python3 -m pytest --cov=report_UI  
cd ../..


cd application/revenue_service
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock
python3 -m pytest --cov=revenue_service   
cd ../..

