import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk12 :
    P2RoundedFactorCheckpointData.panel14Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix48_eq :
    P2RoundedFactorCheckpointData.panel14Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk12.1

theorem panel14Prefix49_eq :
    P2RoundedFactorCheckpointData.panel14Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk12.2.1

theorem panel14Prefix50_eq :
    P2RoundedFactorCheckpointData.panel14Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk12.2.2.1

theorem panel14Prefix51_eq :
    P2RoundedFactorCheckpointData.panel14Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk12.2.2.2

end RHP2Bridge
