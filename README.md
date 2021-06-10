# A project for Programming on the Cloud (COEN 424), Concordia University

This was our biggest project for that course in which we were to demonstrate our ability to build an application using various cloud and big data technologies such as Spark, NoSql, cloud deployments and external pulic APIs.

The focus was more on demonstrating a working proof of concept using the above technologies rather than the completeness of our solutions and we did quite well on this submission. For more information on the requirements please see the Problem-Description.pdf.

Our solution comprised a Node.js server deployed on an AWS EC2 instance. The server had a route each to receive and then display results from a Python script that connected to the Twitter API and used Spark streaming to calculate sentiment by taking each word tweeted and cross referencing against a list of both positive and negative terms then returning a score based on how many postitive or negative terms were used. The chosen topic of Tweets was 'BTC'.

To see more on our solution please refer to the Solution-Report.pdf file.

