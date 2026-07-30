import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk9 :
    P2RoundedFactorCheckpointData.panel11Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix36_eq :
    P2RoundedFactorCheckpointData.panel11Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk9.1

theorem panel11Prefix37_eq :
    P2RoundedFactorCheckpointData.panel11Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk9.2.1

theorem panel11Prefix38_eq :
    P2RoundedFactorCheckpointData.panel11Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk9.2.2.1

theorem panel11Prefix39_eq :
    P2RoundedFactorCheckpointData.panel11Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk9.2.2.2

end RHP2Bridge
