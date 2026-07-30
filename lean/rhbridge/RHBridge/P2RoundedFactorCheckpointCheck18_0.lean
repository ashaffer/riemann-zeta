import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk0 :
    P2RoundedFactorCheckpointData.panel18Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix0_eq :
    P2RoundedFactorCheckpointData.panel18Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk0.1

theorem panel18Prefix1_eq :
    P2RoundedFactorCheckpointData.panel18Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk0.2.1

theorem panel18Prefix2_eq :
    P2RoundedFactorCheckpointData.panel18Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk0.2.2.1

theorem panel18Prefix3_eq :
    P2RoundedFactorCheckpointData.panel18Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk0.2.2.2

end RHP2Bridge
