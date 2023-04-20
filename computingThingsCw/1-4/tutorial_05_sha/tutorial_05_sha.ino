/*
  100% Harry Smith 16048438
*/

#include "mbedtls/md.h" 
 
void hash(const char *input, const size_t inputLength, unsigned char *outputBuffer)

{ 
  mbedtls_md_context_t ctx; 
  mbedtls_md_type_t md_type = MBEDTLS_MD_SHA256; 
  
  mbedtls_md_init(&ctx); 
  mbedtls_md_setup(&ctx, mbedtls_md_info_from_type(md_type), 0); 
  mbedtls_md_starts(&ctx); 
  mbedtls_md_update(&ctx, (const unsigned char *) input, inputLength); 
  mbedtls_md_finish(&ctx, outputBuffer); 
  mbedtls_md_free(&ctx); 
} 
 
void setup()  
{ 
  // put your setup code here, to run once: 
  Serial.begin(9600);  
} 
 
void loop()  
{ 
  // put your main code here, to run repeatedly: 
  char in[32] = "SHA256SHA256SHA256SHA256SHA256!"; 
  unsigned char out[32]; 
   
  hash(in, strlen(in), out);
  Serial.println("Input string: ");
  Serial.println(in);
  Serial.println("Hash output: ");
  for (int i = 0; i < 32; i++) {
    Serial.print(out[i], HEX);
  }
  Serial.println();
  
  delay(15000); 
} 