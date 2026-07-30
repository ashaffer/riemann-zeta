import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk3 :
    P2RoundedFactorCheckpointData.panel6Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix12_eq :
    P2RoundedFactorCheckpointData.panel6Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk3.1

theorem panel6Prefix13_eq :
    P2RoundedFactorCheckpointData.panel6Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk3.2.1

theorem panel6Prefix14_eq :
    P2RoundedFactorCheckpointData.panel6Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk3.2.2.1

theorem panel6Prefix15_eq :
    P2RoundedFactorCheckpointData.panel6Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk3.2.2.2

end RHP2Bridge
