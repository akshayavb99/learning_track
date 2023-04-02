
## What is MLOps?

MLOps is the set of tools and best practices to deploy ML solutions into production.

## What is ML System Design?

- ML System Design involves the design of an end-to-end ML solution starting frm data acquisition to the deployment of the final ML solution into production.
- ML System Design ensures that all the stakeholders for the solution work together to achieve the desired objectived.

## Which problems can be solved by ML?

1. ML solution has the capacity to learn for the problem at hand.
2. ML solution can learn some complex patterns about the problem.
3. ML solution can learn the patterns from some data - data may be available for the direct problem, data may not be available for the problem directly (zero-shot learning), system learns after production deployment from production data (continual learning).
4. The solution to the problem can be framed as a prediction or approximation computed by ML. 
5. The patterns learnt by the ML solution during training are similar to the patterns of new and unseen data - the distributions of seen and unseen data are similar.
6. The problem (and pattern) is repetitve for the ML solution to learn.
7. The cost of predicting wrongly does not outweight the benefits of correct predictions by the ML solution.
8. The problem is at scale - a lot of data can be collected, and the overall prediction can be broken down into a series of predictions.
9. The patterns of the problem constantly change, which make it easier to learn them via ML solutions instead of hard-coded rule-based solutions.
10. The problem can be broken down into smaller problems, one or more of which can be solved with ML. Hence, we can atleast have a solution partially involving ML.

## When are ML solutions not applied?

1. The solution is unethical.
2. Simpler solutions like rule-based solutions provide the required results - no need of additional complexity.
3. The solution is not cost-effective.

## What are some examples of ML use cases?

1. Recommender systems and Search engines
	- Based on users' previous choices, recommend new shows/products
	- Netflix, Amazon
	- 
2. Predictive typing 
	1. Gives suggestions on what can be typed next, based on what is already typed
	2. Whatsapp, Google Docs
3. Fraud Detection
	1. Application of anomaly detection type of ML solutions.
	2. Predict if given transaction is a fraud based on historical fraud transactions.
	3. Banks like Wells Fargo, Bank of America etc.
4. Price Optimization
	1. Estimate price at a given time period to maximize a business objective company margin, revenue etc.
	2. Grocery chains like Walmart, Kroger's
5. Customer Demand Forecast
	1. Predict customer demand based on multiple factors like time of the year, previous year's demands etc.
	2. Helps in preparing budgets, stocking inventory, allocate resources etc.
	3. Grocery chains like Walmart, Costco etc.
6. Acquiring new users
	1. Includes multiple ways of framing the solution
		1. Identifying customers who are likely to buy 
		2. Showing better targeted ads
		3. Predicting right time to offer the right kinds of discounts
	2. Amazon, Walmart
7. Churn Prediction
	1. 
8. Automated Support Ticket Classification
9. Sentiment Analysis