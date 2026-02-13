// Strings
let myName:string = "greeshma";
let myClz:string = "vignan";
let myProjectName:string="AI Resume Builder";
console.log(`I am ${myName} from ${myClz} and my project is ${myProjectName}`);

// number
let myProjectTeam:number = 10;
let myProjectExecutionTime:number=5.5;

// boolean
let isProjectCompleted:boolean = false;
let isProjectInDevelopment:boolean=true;

// undefined
let projectCompetionDate:(undefined|string)=undefined;
projectCompetionDate="30-2-2026";
console.log(`Project Completion Date: ${projectCompetionDate}`);

// any
let storeAnyThing:any;
storeAnyThing="I am learning Typescript";
storeAnyThing=100;
storeAnyThing=true;
console.log("Store Any Things: "+storeAnyThing);

// array
let mySkills:string[]=["html","css","javascript"];
let skillProficiency:number[]=[8,7,6];
let mySkillsAndProficiency:(string|number)[] = ["html",8,"css",7,"javascript",6];
console.log("My Skills: "+mySkillsAndProficiency);

mySkills.push("typescript");
skillProficiency.push(8);
mySkillsAndProficiency.pop();
console.log("After Modification " + mySkills);
console.log("After Modification " + skillProficiency);
console.log("After Modification " + mySkillsAndProficiency);

// tuples
let interviewDetails:[string,string,number][] = [
    ["google","sde-1",45],
    ["microsoft", "sde-1", 45],
    ["Adobe", "sde-1", 45]
];
console.log("Interview Details: "+interviewDetails);
interviewDetails.map((interview) => {
    console.log(interview);
    let [companyName,Role,interviewDuration] = interview;
    console.log("Company Name: " + companyName);
    console.log("Role: "+Role);
    console.log("Interview Duration: "+interviewDuration+ " mins");
})

// objects
let projectDetails:{
    projectName:string,
    projectDescription:string,
    teamSize:number,
    isCompleted:boolean
    // isCompleted?:boolean // (?) it means optional if u don't want to write
} = {
    projectName:"AI Resume Builder",
    projectDescription: "An AI-powered resume builder that helps users create professional resume",
    teamSize:10,
    isCompleted:false
};

console.log("Project Details: ",projectDetails);

// enums
enum ProjectStatus{
    inProgress="Project is in Progress",
    complete="Project is Completed",
    onHold="Project is On Hold"
}

console.log("what is the project Status?");
console.log(ProjectStatus.inProgress);
let projectStatus=ProjectStatus.inProgress;
if(projectStatus==="Project is in Progress"){
    console.log("Project is being delayed");
}

// interfaces

interface StudentDetails{
    studentName:string,
    studentRollNo:number
}

let a:StudentDetails={studentName:"greeshma",studentRollNo:3};

interface ProjectDetailsInterface
{
    ProjectFullName:string,
    ProjectFullDescription:string,
    ProjectStack:string[],
    ProjectFeatures:string[]
}
console.log("Student Details: ",a);
let myProject:ProjectDetailsInterface={
    ProjectFullName:"AI resume builder",
    ProjectFullDescription:"An AI-powered resume builder that helps users create professional resume",
    ProjectStack:["html","css","javascript","typescript","node.js"],
    ProjectFeatures:["Resume Parsing","Template Selection","Real-time Collaboration"]
}

console.log("My Project tech stack",myProject.ProjectStack);

// functions
function addTwoNumbers(a:number,b:number):number{
    return a+b;
}

console.log("Additionof 2 and 3 is: "+addTwoNumbers(2,3));
console.log("Addition of 5 and 4 is: "+addTwoNumbers(5,4));
function Intro(name:string,clz:string,studyingIn:number):void
{
    console.log("I am "+name+" from "+clz+" studying in "+studyingIn+" year.");
}

console.log(Intro("greeshma","vignan",3));

// try-catch
function Trail(raiseError:boolean):void {
    try {
        if(raiseError)
        {
            throw new Error("An error occured");
        }
        else {
            console.log("No Error");
        }
    } catch (error) {
        console.log("Error Caught:", error);
    }
}
Trail(false);
Trail(true);