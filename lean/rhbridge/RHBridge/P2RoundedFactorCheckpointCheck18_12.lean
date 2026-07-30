import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk12 :
    P2RoundedFactorCheckpointData.panel18Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix48_eq :
    P2RoundedFactorCheckpointData.panel18Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk12.1

theorem panel18Prefix49_eq :
    P2RoundedFactorCheckpointData.panel18Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk12.2.1

theorem panel18Prefix50_eq :
    P2RoundedFactorCheckpointData.panel18Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk12.2.2.1

theorem panel18Prefix51_eq :
    P2RoundedFactorCheckpointData.panel18Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk12.2.2.2

end RHP2Bridge
