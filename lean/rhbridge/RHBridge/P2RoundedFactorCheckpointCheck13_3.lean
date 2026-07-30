import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk3 :
    P2RoundedFactorCheckpointData.panel13Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix12_eq :
    P2RoundedFactorCheckpointData.panel13Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk3.1

theorem panel13Prefix13_eq :
    P2RoundedFactorCheckpointData.panel13Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk3.2.1

theorem panel13Prefix14_eq :
    P2RoundedFactorCheckpointData.panel13Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk3.2.2.1

theorem panel13Prefix15_eq :
    P2RoundedFactorCheckpointData.panel13Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk3.2.2.2

end RHP2Bridge
