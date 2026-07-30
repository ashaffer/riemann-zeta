import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk3 :
    P2RoundedFactorCheckpointData.panel14Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix12_eq :
    P2RoundedFactorCheckpointData.panel14Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk3.1

theorem panel14Prefix13_eq :
    P2RoundedFactorCheckpointData.panel14Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk3.2.1

theorem panel14Prefix14_eq :
    P2RoundedFactorCheckpointData.panel14Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk3.2.2.1

theorem panel14Prefix15_eq :
    P2RoundedFactorCheckpointData.panel14Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk3.2.2.2

end RHP2Bridge
