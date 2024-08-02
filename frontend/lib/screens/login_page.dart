import 'package:flutter/material.dart';
import 'package:frontend/components/text_field.dart';
import 'package:frontend/controllers/loginController.dart';
import 'package:get/get.dart';
import 'package:go_router/go_router.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  LoginController controller = Get.put(LoginController());
  final usernameController = TextEditingController();
  final passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[200],
      body: SafeArea(
        child: Center(
          child: Column(
            mainAxisSize: MainAxisSize.max,
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
                        'Please enter your credentials to log in',
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 10),
              Expanded(
                child: ListView(
                  padding: const EdgeInsets.symmetric(horizontal: 24.0),
                  children: [
                    Container(
                      width: double.infinity,
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
                            controller: controller.username,
                            hintText: 'eg. John Doe',
                            obscureText: false,
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 16),
                    Container(
                      width: double.infinity,
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
                            controller: controller.password,
                            hintText: 'eg. password',
                            obscureText: true,
                          ),
                        ],
                      ),
                    ),
                    Align(
                      alignment: Alignment.centerRight,
                      child: Padding(
                        padding: const EdgeInsets.fromLTRB(0, 10, 30, 10),
                        child: TextButton(
                          onPressed: () {
                            // To be implemented later
                          },
                          style: TextButton.styleFrom(
                            foregroundColor: Colors.blue[800], backgroundColor: Colors.transparent,
                            side: BorderSide.none,
                          ),
                          child: const Text('Forgot Password?', style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold),),
                        ),
                      ),
                    ),
                    SizedBox(
                      width: double.infinity,
                      height: 50,
                      child: TextButton(
                        onPressed: () async {
                          await controller.submit(context);
                        },
                        style: TextButton.styleFrom(
                          foregroundColor: Colors.white,
                          backgroundColor: Colors.blue[700],
                          side: BorderSide.none,
                        ),
                        child: const Text('Login', style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold),),
                      ),
                    ),
                    Row(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        const Text('Don\'t have an account?'),
                        TextButton(
                          onPressed: () {
                            context.go("/signup");
                          },
                          style: TextButton.styleFrom(
                            foregroundColor: Colors.blue[800], backgroundColor: Colors.transparent,
                            side: BorderSide.none,
                          ),
                          child: const Text('Sign up', style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold),),
                        ),
                      ],
                    )
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
