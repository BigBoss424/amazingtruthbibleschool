import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

//Add other SDK's that need to be implemented into the site. 

//Firebase web app's configuration
const firebaseConfig = {

  apiKey: "AIzaSyBO1aGXQprrtPfNYM2FARtj5i1NOx5Ihb4",

  authDomain: "amazing-truth-bible-school.firebaseapp.com",

  databaseURL: "https://amazing-truth-bible-school-default-rtdb.firebaseio.com",

  projectId: "amazing-truth-bible-school",

  storageBucket: "amazing-truth-bible-school.appspot.com",

  messagingSenderId: "722057521324",

  appId: "1:722057521324:web:52966cdf5d4c3437bf9709",

  measurementId: "G-JVQG2RH9M7"

};

//Initialize Firebase 
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);


