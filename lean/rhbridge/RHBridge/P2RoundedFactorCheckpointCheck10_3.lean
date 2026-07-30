import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk3 :
    P2RoundedFactorCheckpointData.panel10Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix12_eq :
    P2RoundedFactorCheckpointData.panel10Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk3.1

theorem panel10Prefix13_eq :
    P2RoundedFactorCheckpointData.panel10Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk3.2.1

theorem panel10Prefix14_eq :
    P2RoundedFactorCheckpointData.panel10Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk3.2.2.1

theorem panel10Prefix15_eq :
    P2RoundedFactorCheckpointData.panel10Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk3.2.2.2

end RHP2Bridge
