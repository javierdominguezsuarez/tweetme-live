import {useState} from 'react'

const useApiCallback = (apiFunc, callback) => {
  
    const [data, setData] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(false)

    const request = async (...args) => {

        setLoading(true)
        
        const data = await apiFunc(...args)

        
        if(!data.ok){
          setError(true)
        }
    
        setData(data.data)

        /*
        if(data.ok){
          console.log(data.data)
          callback(data.data)
        }
        */

        console.log(data.data)
        callback(data.data)
        

        setLoading(false)
    
      }
    
    return {data, error, loading, request}
}

export default useApiCallback