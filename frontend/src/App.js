import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Col, Container, Form, Spinner } from 'react-bootstrap';
import { AiFillPicture } from "react-icons/ai";
import WriteTweet from './Components/WriteTweet';
import Tweet from './Components/Tweet';
import Pallete from './Components/Pallete';
import useApiCallback from './customHooks/useApiCallback'
import axios from 'axios';
import { useEffect, useState} from 'react';
function App() {


  const [tweets, setTweets] = useState()
  const request = useApiCallback(() => axios.get('http://127.0.0.1:8000/tweets/'), (data) => setTweets(data))


  useEffect(() => {
    request.request()
  }, [])

  function reload(){
    request.request()
  }

  if(request.loading)
    return (<Spinner variant="light"></Spinner>)


  return (
    <div className="App" style={{backgroundColor : Pallete.primary}}>
      <div className="container p-4">
        <WriteTweet reload={() => reload()}></WriteTweet>

        {
        tweets.map(obj => <Tweet obj={obj}/>)
        }



      </div>
    </div>
  );
}

export default App;
