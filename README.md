# AutomationTestChallenge
1. Before run test you need to install python 3 and pip3. Please help me download it, before run test
- Link download python 3: https://www.python.org/downloads/
- Install pip3: python3 -m pip install --upgrade pip
2. Open project and go to terminal:
 - Run command line: pip3 install -r requirements.txt (It will install the package which need to run test)
3. Run test Filter with Inactive:
 - Run command line: pytest --html=Report/test_filter.html Tests/test_FilterFunction.py
4. Run test Sort First Name:
 - Run command line: pytest --html=Report/test_sort.html Tests/test_SortColumnData.py
5. Run test API:
 - Run command line: pytest --html=Report/test_api.html APITests/test_API.py
