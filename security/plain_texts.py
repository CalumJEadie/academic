# Group Project Requirements Specification
# Non Ascii characters removed

p1 = """Requirements Specification
General investigation of the problem and its background
Background
A plant consists of many physical machines with different physical characteristics; prominently the properties of the CPU and main memory. Each physical machine may be host to several virtual machines or may host several applications natively. Similarly each virtual machine may host several applications.
In a plant there is potential for elasticity and resource balancing. This refers to the ability to transfer applications or virtual machines between machines.
In order for an administrator to decide how to distribute resources it is necessary for them to be able to analyse the resource usage of applications over time.
Problem
The task of distributing resources involves considering many different combinations of machines and applications. Furthermore it involves many different variables describing the characteristics of host machine and application. It is difficult for an administrator to make good use of the available resources as there is so much information to consider.
A part of distributing resources effectively involves being able to monitor the current plant and predict the future resource usage. Similarly this is a task that involves a great amount of information and is difficult to carry out for the many machines and applications in a plant.
One method to monitor the resource usage is to analyse graphs of resource metrics. This method is problematic in that it requires manual consideration of many graphs (for the many machines and applications) over many periods of time (to be able to consider short and long term trends).
User analysis
From considering the context the tools described in the client brief would be used in it is anticipated that the primary users will be System Administrators.
Key attributes and needs of a System Administrator
Efficient interface in the tools they use
The ability to quickly interact with tools is of much more important than aesthetics.
Flexibility and configurability in tools they use
System Administrators are accustomed to solving problems using existing tools as starting point.
For example using cron to periodically grep the contents of a log file and use an email client to notify them of important events.
The key point is that each of the tools is sufficiently flexible and configurable to be able to used as part of a larger solution and to adapt to their work flow.
Technical detail
The more detail tools can potentially give the more useful they can be potentially be.
It is important for the level of detail of tools to be configurable however the key point is that tools must be capable of a great level of technical detail.
Facilities to be provided
We will produce a resource evaluation tool for the purpose of analysing and optimising resource usage within a cloud platform plant. There will be three main facilities provided:
Trend detection
Application redistribution / rebalancing
Application placement tool
Trend detection
Part of the tool will be a trend detection module which will be able to detect periodic and long term trends in the input data. From this it will be able to inform the user of any trends (periodic or long term) that are detected and are statistically probable, according to the threshold determined by the user. It will also be able to perform simple extrapolation based on the trends and warn the user if the projected usage exceeds the maximum available resources of the host machine.
The tool will output in simple text to will allow it to be used with other Unix utilities and scripts. On request, it will also be able to provide a report in either HTML or text, which shows the predicted resource usage in the future, and any detected trends which may be of interest to the user.
Application redistribution / rebalancing
On top of this the tool will be able to use the analysis previously undertaken to deduce the most efficient distribution of applications across available hosts. This will be done by considering the resources used by each application and the resources available on each host, taking into consideration a user specified cost for relocating applications.
Placement tool
As well as being able to rebalance the load, the tool will also be able to provide a suggestion of the optimal host for a new application, given an indicator of the resource requirements of the new application. The user will be able to specify the extent to which existing applications may be reshuffled in order to provide a more balanced solution.
Interface
From the user analysis, we expect the user to be a system administrator so an efficient interface is required. We assume they will be proficient at using command line tools, so this will be the optimal interface for the program as it will enable the product to be scripted and automated e.g. in a cron job.

Acceptance criteria
The acceptance criterion has been developed from the features to be provided and feasibility research.
Deadlines
Client Meeting 1 - 02/02/2012: Specification and project plan.
Client Meeting 2 - 16/02/2012: Progress report on implementation and testing.
Client Meeting 3 - 02/03/2012: Group report and personal reports.
Major functions
Placement optimisation
The placement optimisation has two main uses: optimising the whole plant and finding a suitable placement for a new application. General criteria for the optimisation module are detailed below, followed by specific criteria for the two dependant components.
1. The system will suggest a new placement of applications onto servers that satifies the following constraint: we satisfy the resource demands of all applications as well as possible by trying to distribute the resources left on the servers such that:
a. The excess capacity of hosts is evenly distributed.
b. Applications which primarily rely on a particular resource will be placed on a host that has relatively large excess capacity for this resource.
2. In all decisions provided, the quality of the suggestion will depend on the quality of the input. In particular, the amount of historic data or the quality of resource usage estimations as typed in by the user is expected to have a high influence on how useful the placement suggestion of our tool will be.
3. The user can enter new applications together with expected resource demands. The system will then suggest a new placement of applications.
4. We will provide the ability for the user to define a penalty for moving applications between servers. Then, a good placement decision also includes a number of application movements. By choosing a high penalty for moving applications, the user has the ability forbid the tool to vary the existing placement, but only decide on which host the new application should be deployed.
5. The optimizer will work only using application resource usage data. No application-specific metrics will be taken into account.
6. Whole plant optimisation:
a. The user will execute a command line tool specifying an input file containing 1 month of resource usage history as an argument.
b. The tool will process the history and available resources to assess the current free resource distribution.
c. The tool will optimise the distribution of applications across the available resources subject to the resource constraints taking into account a fixed penalty specified by the user for moving applications.
d. It will output a placement decision in plain text.
e. If specified, a report will be output in simple HTML detailing the placement report.
f. If no placement satisfying the resource constraints is found, the tool will output an error.
g. On receiving malformed/incomplete input, the tool will print an error message and halt.
7. New application placement:
a. The user will execute a command line tool specifying an input file containing 1 month of resource usage history as an argument, and another file detailing the new application's resource requirements.
b. The tool will process the history and available resources to produce an optimal allocation suggestion for the new application, upon request from the user.
c. The tool will output a simple placement decision in plain text.
d. If specified, a report will be output in simple HTML detailing the placement report.
e. If no placement satisfying the resource constraints is found, the tool will output an error.
f. On receiving malformed/incomplete input, the tool will print an error message and halt.
Trend analysis
1. The tool will then search for dangerous trends and a time in the future, when one or more trends are likely to cause a server to not be able to satisfy the requirements of applications
2. For this time in the future, the tool will suggest an alternative placement. This new placement then allows the user to reschedule applications in advance to ensure that applications will not break down during peak times in the future.
3. Trend Detection criteria:
a. The user will execute a command line tool specifying an input file containing 1 month of resource usage history as an argument.
b. The tool will analyse the resource history, looking for periodic and linear trends.
c. By default, if found, the trends will be output in text with one trend per line, each line containing the parameters of the trend and the estimated statistical confidence value.
d. If specified, a report will be output in simple HTML detailing and graphing the detected trends.
e. As well as this, the report may optionally include warnings about predicted resource usage highlighted in an appropriate manner.
f. On receiving malformed/incomplete input, the tool will print an error message and halt.
Appearance
1. All functionality will be provided through a command line tool
Input/Output
1. Input will take the form of files specified on the command line, as well as a configuration file that will be loaded each time the tool is run.
2. Specific parameters for tool usage will be entered as predefined arguments to the command line tool.
Config input file
1. The configuration file will contain a user specific value representing the approximated administration cost of relocating any currently running applications.
2. It may also contain other general settings/adjustments.
Data input file
The following inputs may be provided in the form of an input file:
1. A list of resource types and their corresponding unit.
2. A list of hosts with their resource limitations and currently resident applications.
3. For each application and the resources it uses, an expected/typical usage value and/or a trace of the applications usage for that resource.
4. The relative importance weighting of resources for a given application.
Output
1. Output is provided via text and html files.
2. Output provides suggestions regarding placement/relocation decisions and/or possibly dangerous trends with an indication of the strength of each trend.
Personnel level required to use the product
1. Familiarity with command line tools is expected as the user is expected to be a system administrator.
2. Man pages/documentation will be provided.
Capacity, accuracy and availability
1. When the tool provides a placement decision or rearrangement, the placement decisions will be accurate enough that if implemented, the applications will function without exceeding available resources within the foreseeable future, provided the input data truly reflects their typical resource usage and no unexpected events occur.
2. The tool will provide solutions only when run, no real time monitoring will be provided, though it should be possible to automate the tool by use of a script so that it can be scheduled to run periodically.
Reliability
1. The reliability of the output will be completely dependant on the reliability and availability of the input data.
2. When outputting detected trends, each one will be accompanied by an indicator of the reliability of that trend.
3. All functionality will be thoroughly tested.
Running costs
1. The running time for the tool will increase with the number of hosts and applications, but should not exceed 1hr in all practical uses.
Security/Ease of use
1. Good programming practice and standards will be used to avoid trivial security issues.

Algorithms and libraries research
Research into algorithms and libraries has been carried out early into the project to determine the feasibility of trend detection and placement optimization. 
Trend detection
The Apache Math library includes a set of statistical classes that perform functions such as error handling interpolation and curve fitting which could be extremely useful during the data analysis stage of operation. Linear regression and possibly extending to polynomial analysis will be required when performing the trend detection and prediction. A possible extension of this, provided we have enough time, is use of genetic algorithms in the Apache library to implement the machine learning to deal with both short and long-term trends (entirely non essential). We are anticipating data to be given to us in some form of fairly advanced text files such as XML and this will require parsing. However, this task is extremely common, so there are quite a few libraries to deal with it such as JDOM Project. Processing resource usage history is a fairly trivial task as the system will provide a snapshot of the current usage on all the hosts across the plant and then these can be stored and retrieved to recreate the history of usage.
Placement optimisation
Algorithms
The group thinks that linear programming algorithms are a suitable approach for this problem. The problem of finding optimal placements defines a set of constraints, for example
sum of expected resource demands of all applications scheduled on a host must not exceed the resources of the host
each application must be scheduled on exactly one host.
The objective function to be optimized will incorporate our way of scoring placements (cf. acceptance criteria). It will also use weighting factors for metrics given by the user (e.g. how important RAM for a particular application is, which will influence how much extra unused RAM will be provided on the host it's placed on). Also, we will specify internal weighting functions to express the fact that it is a lot worse to use, for instance, 80% instead of 70% RAM on a certain host, compared to using 30% instead of 20%. The set of constraints, together with the formula to optimize, can then be fed into a linear (integer) optimizer. The decision variables for this problem include N*M binary variables x_ij, where N is the number of applications and M is the number of servers. x_ij is 1 iff application i is placed on host j, and 0 else. Using this notion, we will be able to retrieve the placement after the optimization is finished.
Libraries
We are going to make use the "GNU Linear Programming Kit" (http://www.gnu.org/software/glpk/). It is a widely-used and thoroughly-tested set of linear programming algorithms, including simplex methods. There are multiple Java interfaces that allow using GLPK functionality within Java code. We decided to use "GLPK for Java" (http://glpk-java.sourceforge.net/) since it seems to be the most popular one. In addition to that, we might consider using the "Linear Optimization Wrapper for Java" (http://www.xypron.de/projects/linopt/) which provides a simple wrapping around the "GLPK for Java" binding. However, it may turn out that we need access to the parts of the GLPK which aren't accessible via the wrapper. All of the software mentioned above is open-source.

System design
Our system design can be split up into three main parts trend analysis, placement optimisation and data representation.
Data Representation
The plant class provides the main abstraction for data representation in out system. It holds all information associated with a plant, namely a set of hosts, applications and a current placement in the form of map from applications to hosts. New applications that shall be placed in the plant are in the set of application, but not in the domain of the map.
A host object has a set of available resources, while each application has a set of used resources. Resources are uniquely identified by an associated ResourceType object, so that, for example, all historical CPU load information for different applications are internally recognized to refer to the same resource. This is crucial for the optimiser to make placement decisions.
UsedResource is an abstract superclass which represents one particular resource used by one particular application. It has either a sample trace (UsedResourceHistory), or just a single expected value (UsedResourceExpectedValue).
The InputParser provides functionality to process an input file and convert it into objects as described above.
Placement
The optimiser class provides a public method which takes a plant object and a config (in which, e.g., the penalty for moving applications is specified) and returns a new mapping. Internally, it will convert the object data into arrays of parameters which can then be fed into the external linear optimization library by a private function. In case there are gaps in the data (e.g. resource usage not specified), it will assume default values. Also, in case there are sample traces, it will do averaging to obtain estimated demands since the linear optimisation function needs exactly one resource usage value per application for every resource.
The PlacementChangeReportGenerator takes two placements and generates a report saying which applications have been moved between which hosts.
Trend analysis
The TrendDetector provides a method that takes a Plant object and returns a set of Trend objects. Trend is an abstract superclass with subclasses LinearTrend and PeriodicTrend. It will return one Trend for every application-resource pair. In case of inconclusive results while trying to find trends, the predicted trend will be a constant. After the trends have been detected, the detection method will automatically classify them using a private method. The classification will be based on whether and when a trend causes a resource to be exhausted.
In case the user wants to obtain suggestions for a new placement which is safe for the future, the DataPredictor will produce a Plant object which represents the predicted state at some future point in time (e.g. when the first trend causes resource demands on one server to exceed capacity), based on currently known trends. This predicted plant state can then be fed into the optimiser.
Structure diagram


Class diagram

Input Format
It has been identified that some sort of hierarchal representation of the input data necessary. Potentially this could be achieved with XML, examples follow.
config.xml
<resourcetypes>
	<resourcetype>
		<id></id>
		<name></name>
		<unit></unit>
	</resourcetype>
</resourcetypes>

plant.xml
<hosts>
	<host>
		<name>_hostname_</name>
		<available_resources>
			<available_resource>
				<id></id>
				<value></value>
			</available_resource>
			<available_resource>
				<id></id>
				<value></value>
			</available_resource>
		</available_resources>

		<application>
			<application_name>_appname_</application_name>
			<resources_used>
				<resource>
					<resourceid>_resourceid_</resourceid>
					<importance>_importancefactor</importance>
					<resource_trace> % optional
						<samples>
							<sample>
								% times are to be provided in UNIX time format (seconds)
								<time>_timeofsample_</time>
								<value>_valueofsample_</value>
							</sample>
							<sample>
								<time>_timeofsample_</time>
								<value>_valueofsample_</value>
							</sample>
							<sample>
								<time>_timeofsample_</time>
								<value>_valueofsample_</value>
							</sample>
						</samples>
					</resource_trace>
					<expected_value>_expected_value_</expected_value> % optional, but should be provided in case no historical data available
				</resource>
				<resource>
					...
				</resource>
			</resources_used>
		</application>
		<application>
			..
		</application>
	</host>

	<host>
		...
	</host>
</hosts>

Pseudo code for application control logic
To illustrate the flow of control and data between components basic pseudocode has been created for the application main method.
Configuration config = ConfigParser.parse(<config_path>);

Plant p = InputParser.parse(<input_file_path>, config);

if(optimise) {
	if(new_application_to_be_scheduled) {
		new_applications = InputParser.parseNewApps(<new_applications_file>);
		p.addNewApplications(new_applications);
	}

	Map<Application, Host> newPlacement = Optimiser.optimise(p);
	String changeReport = ChangeReportGenerator.generateChangeReport(p.getPlacement(), newPlacement);
} else if(trend detect) {
	Set<Trend> trends = TrendDetector.detectTrends(p);

	string report = TrendReportGenerator.generateReport(trends, p.getPlacement(), <report_level>, <report_format>);

	System.out.println(report);

	if(predict_data) {
		// search for a time
		for(Trend t: trends) {
			// get running minimum of point of crisis
			critical_time = ...
		}

		Plant dangerousPlantState = DataPredictor.predict(p, trends, critical_time);

		// find an alternative placement for this time; the optimiser will have encoded in its constraints that no capacities are exceeded, so the new placement is guaranteed to be safe
		Map<Application, Host> newPlacement = Optimiser.optimise(dangerousPlantState);

		String changeReport = ChangeReportGenerator.generateChangeReport(p.getPlacement(), newPlacement);

	}
}

Management strategy 
Management Approach
Calum will have the role of Group Leader. He will be the primary point of contact for the client and group project leaders.
The entire group will meet every Tuesday and Thursday to discuss progress. Meeting will be as brief and efficient as possible. Minutes will be taken to facilitate review. The group, or subsets of, will meet at other times where necessary. Similarly meetings will be focused and relevant discussion recorded.
The group will communicate through a group mailing list to maintain cohesion and to bring any points of contention immediately to the group's attention. This will allow the group to identify and deal with problems early.  Where possible members of the group will write up relevant research and discussions and make them available to the rest of the group.  This will avoid duplication of effort and keep the group informed of progress. The GitHub Wiki will provide a good environment for this as it provides collaborative editing.
Management tools
To facilitate effective management of the project the following tools will be used.
GroupSpaces
The group management tool GroupSpaces will be used to provide a mailing list for the group to facilitate effective communication.
GitHub
The project management tool GitHub will provide many capabilities. Notably it will provide version control for the source code, documentation and other file types as appropriate. The issue tracking system it provides will be used to keep a record of upcoming and completed tasks. The Wiki will provide an environment where documentation can be collaboratively edited. 
Gantter
The project planning tool Gantter will be used to maintain an overall picture of project progress. This will provide the ability to express dependencies between tasks, expected task length and current time elapsed on a task."""

p2 = p1.lower()

p3 = p1.upper()

# Uppercase and with non alpha characters removed.
p4 = filter(str.isalpha,p3)