import { GoogleLogin } from '@react-oauth/google';

export function Home(){

    const ConfirmLogin = () => {
        window.alert("Login Successful!");
    }

    const handleError = () => {
    window.alert("Login FAILED!");
  };

    return (

        <div className="container">
            <header className="page-header">
            <h1>Home.</h1>
            </header>
            <div className="flex h-screen w-full items-center justify-center bg-gray-100">

            <GoogleLogin
                onSuccess={ConfirmLogin}
                onError={handleError}
                useOneTap
            />
            </div>
        </div>
    )
}