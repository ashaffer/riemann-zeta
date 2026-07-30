import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk12 :
    P2RoundedFactorCheckpointData.panel31Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix48_eq :
    P2RoundedFactorCheckpointData.panel31Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk12.1

theorem panel31Prefix49_eq :
    P2RoundedFactorCheckpointData.panel31Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk12.2.1

theorem panel31Prefix50_eq :
    P2RoundedFactorCheckpointData.panel31Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk12.2.2.1

theorem panel31Prefix51_eq :
    P2RoundedFactorCheckpointData.panel31Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk12.2.2.2

end RHP2Bridge
