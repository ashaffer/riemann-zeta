import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk12 :
    P2RoundedFactorCheckpointData.panel2Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix48_eq :
    P2RoundedFactorCheckpointData.panel2Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk12.1

theorem panel2Prefix49_eq :
    P2RoundedFactorCheckpointData.panel2Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk12.2.1

theorem panel2Prefix50_eq :
    P2RoundedFactorCheckpointData.panel2Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk12.2.2.1

theorem panel2Prefix51_eq :
    P2RoundedFactorCheckpointData.panel2Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk12.2.2.2

end RHP2Bridge
