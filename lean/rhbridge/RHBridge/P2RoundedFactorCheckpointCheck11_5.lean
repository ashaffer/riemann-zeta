import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk5 :
    P2RoundedFactorCheckpointData.panel11Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix20_eq :
    P2RoundedFactorCheckpointData.panel11Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk5.1

theorem panel11Prefix21_eq :
    P2RoundedFactorCheckpointData.panel11Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk5.2.1

theorem panel11Prefix22_eq :
    P2RoundedFactorCheckpointData.panel11Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk5.2.2.1

theorem panel11Prefix23_eq :
    P2RoundedFactorCheckpointData.panel11Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk5.2.2.2

end RHP2Bridge
