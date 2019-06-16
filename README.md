# Time Format Convertor
this project is created as a part of hiring process.

## Usage
You can find a basic example in example.py file in the root of this project. Note that you have to have package re installed.
```
import timeConversionTask

input = "blabla 01:42:12PM bla bla blablabla bla"

# use first function to extract time from text
extractedTime = timeConversionTask.extractTime(input)
# use second function to convert time from 12 hour to 24 hour format
convertedTime = timeConversionTask.convertTimeFormat(extractedTime)
# print converted time
print(convertedTime)
```
## Output
You will see converted time in 24 hour format. In this case it will be: 13:42:12.
