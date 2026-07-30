import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk3 :
    P2RoundedFactorCheckpointData.panel15Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix12_eq :
    P2RoundedFactorCheckpointData.panel15Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk3.1

theorem panel15Prefix13_eq :
    P2RoundedFactorCheckpointData.panel15Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk3.2.1

theorem panel15Prefix14_eq :
    P2RoundedFactorCheckpointData.panel15Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk3.2.2.1

theorem panel15Prefix15_eq :
    P2RoundedFactorCheckpointData.panel15Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk3.2.2.2

end RHP2Bridge
