import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk3 :
    P2RoundedFactorCheckpointData.panel9Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix12_eq :
    P2RoundedFactorCheckpointData.panel9Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk3.1

theorem panel9Prefix13_eq :
    P2RoundedFactorCheckpointData.panel9Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk3.2.1

theorem panel9Prefix14_eq :
    P2RoundedFactorCheckpointData.panel9Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk3.2.2.1

theorem panel9Prefix15_eq :
    P2RoundedFactorCheckpointData.panel9Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk3.2.2.2

end RHP2Bridge
