import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk0 :
    P2RoundedFactorCheckpointData.panel11Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix0_eq :
    P2RoundedFactorCheckpointData.panel11Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk0.1

theorem panel11Prefix1_eq :
    P2RoundedFactorCheckpointData.panel11Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk0.2.1

theorem panel11Prefix2_eq :
    P2RoundedFactorCheckpointData.panel11Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk0.2.2.1

theorem panel11Prefix3_eq :
    P2RoundedFactorCheckpointData.panel11Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk0.2.2.2

end RHP2Bridge
