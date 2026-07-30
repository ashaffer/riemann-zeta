import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk12 :
    P2RoundedFactorCheckpointData.panel13Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix48_eq :
    P2RoundedFactorCheckpointData.panel13Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk12.1

theorem panel13Prefix49_eq :
    P2RoundedFactorCheckpointData.panel13Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk12.2.1

theorem panel13Prefix50_eq :
    P2RoundedFactorCheckpointData.panel13Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk12.2.2.1

theorem panel13Prefix51_eq :
    P2RoundedFactorCheckpointData.panel13Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk12.2.2.2

end RHP2Bridge
