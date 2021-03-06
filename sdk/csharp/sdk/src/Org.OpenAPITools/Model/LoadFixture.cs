/* 
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// LoadFixture
    /// </summary>
    [DataContract]
    public partial class LoadFixture :  IEquatable<LoadFixture>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="LoadFixture" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected LoadFixture() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="LoadFixture" /> class.
        /// </summary>
        /// <param name="fixture">fixture (required).</param>
        /// <param name="mode">mode.</param>
        /// <param name="encoding">encoding.</param>
        public LoadFixture(string fixture = default(string), string mode = default(string), string encoding = default(string))
        {
            // to ensure "fixture" is required (not null)
            if (fixture == null)
            {
                throw new InvalidDataException("fixture is a required property for LoadFixture and cannot be null");
            }
            else
            {
                this.Fixture = fixture;
            }
            
            this.Mode = mode;
            this.Encoding = encoding;
        }
        
        /// <summary>
        /// Gets or Sets Fixture
        /// </summary>
        [DataMember(Name="fixture", EmitDefaultValue=true)]
        public string Fixture { get; set; }

        /// <summary>
        /// Gets or Sets Mode
        /// </summary>
        [DataMember(Name="mode", EmitDefaultValue=false)]
        public string Mode { get; set; }

        /// <summary>
        /// Gets or Sets Encoding
        /// </summary>
        [DataMember(Name="encoding", EmitDefaultValue=false)]
        public string Encoding { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class LoadFixture {\n");
            sb.Append("  Fixture: ").Append(Fixture).Append("\n");
            sb.Append("  Mode: ").Append(Mode).Append("\n");
            sb.Append("  Encoding: ").Append(Encoding).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as LoadFixture);
        }

        /// <summary>
        /// Returns true if LoadFixture instances are equal
        /// </summary>
        /// <param name="input">Instance of LoadFixture to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(LoadFixture input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Fixture == input.Fixture ||
                    (this.Fixture != null &&
                    this.Fixture.Equals(input.Fixture))
                ) && 
                (
                    this.Mode == input.Mode ||
                    (this.Mode != null &&
                    this.Mode.Equals(input.Mode))
                ) && 
                (
                    this.Encoding == input.Encoding ||
                    (this.Encoding != null &&
                    this.Encoding.Equals(input.Encoding))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Fixture != null)
                    hashCode = hashCode * 59 + this.Fixture.GetHashCode();
                if (this.Mode != null)
                    hashCode = hashCode * 59 + this.Mode.GetHashCode();
                if (this.Encoding != null)
                    hashCode = hashCode * 59 + this.Encoding.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            // Mode (string) maxLength
            if(this.Mode != null && this.Mode.Length > 10)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for Mode, length must be less than 10.", new [] { "Mode" });
            }

            
            // Encoding (string) maxLength
            if(this.Encoding != null && this.Encoding.Length > 10)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for Encoding, length must be less than 10.", new [] { "Encoding" });
            }

            
            yield break;
        }
    }

}
