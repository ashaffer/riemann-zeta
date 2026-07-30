import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk0 :
    P2RoundedFactorCheckpointData.panel21Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix0_eq :
    P2RoundedFactorCheckpointData.panel21Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk0.1

theorem panel21Prefix1_eq :
    P2RoundedFactorCheckpointData.panel21Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk0.2.1

theorem panel21Prefix2_eq :
    P2RoundedFactorCheckpointData.panel21Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk0.2.2.1

theorem panel21Prefix3_eq :
    P2RoundedFactorCheckpointData.panel21Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk0.2.2.2

end RHP2Bridge
