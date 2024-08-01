import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../components/text_field.dart';


class SignupPage extends StatefulWidget {
  const SignupPage({super.key});

  @override
  State<SignupPage> createState() => _SignupPageState();
}

class _SignupPageState extends State<SignupPage> {

  final emailController = TextEditingController();
  final usernameController = TextEditingController();
  final passwordController = TextEditingController();
  final confirmPassword = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[200],
      body: SafeArea(
        child: Center(
          child: Column(
            children: [
              const SizedBox(height: 80),
              const Icon(Icons.book, size: 80),
              const Text(
                'Blog App',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 20),
              const Align(
                alignment: Alignment.centerLeft,
                child: Padding(
                  padding: EdgeInsets.fromLTRB(20, 20, 0, 20),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.start,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Let\'s go!',
                        style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold),
                      ),
                      Text(
                        'Create a new account',
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                ),
              ),

              const SizedBox(height: 10,),


              Container(
                width: 350,
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(8),
                ),

                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [
                    Text(
                      'Enter Email ID',
                      style: TextStyle(fontSize: 16, color: Colors.grey.shade800),
                    ),
                    GenTextField(
                      controller: passwordController,
                      hintText: 'eg. abc@gmail.com',
                      obscureText: true,
                    ),
                  ],
                ),
              ),


              const SizedBox(height: 10),

              Container(
                width: 350,
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Enter user name',
                      style: TextStyle(fontSize: 16, color: Colors.grey.shade800),
                    ),


                    const SizedBox(height: 8),

                    GenTextField(
                      controller: usernameController,
                      hintText: 'eg. John Doe',
                      obscureText: false,
                    ),
                  ],
                ),
              ),



              const SizedBox(height: 16),


              Container(
                width: 350,
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(8),
                ),

                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [
                    Text(
                      'Enter password',
                      style: TextStyle(fontSize: 16, color: Colors.grey.shade800),
                    ),
                    GenTextField(
                      controller: passwordController,
                      hintText: 'eg. password',
                      obscureText: true,
                    ),
                  ],
                ),
              ),

              const SizedBox(height: 13,),

              SizedBox(
                width: 350,
                height: 50,
                child: TextButton(
                  onPressed: (){
                    // Sign Up function
                  },

                  style: TextButton.styleFrom(

                    foregroundColor: Colors.white,
                    backgroundColor: Colors.blue[700],
                    side: BorderSide.none,
                  ),
                  child: const Text('Sign up', style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold),),
                ),
              ),


              SizedBox(
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Text('Already have an account?'),
                    TextButton(
                      onPressed: () {
                        context.go("/login");
                      },
                      style: TextButton.styleFrom(
                        foregroundColor: Colors.blue[800], backgroundColor: Colors.transparent,
                        side: BorderSide.none,
                      ),
                      child: const Text('Login', style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold),),
                    ),
                  ],
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
