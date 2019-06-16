import timeConversionTask

input = "blabla 01:42:12PM bla bla blablabla bla"

# use first function to extract time from text
extractedTime = timeConversionTask.extractTime(input)
# use second function to convert time from 12 hour to 24 hour format
convertedTime = timeConversionTask.convertTimeFormat(extractedTime)
# print converted time
print(convertedTime)