import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk7 :
    P2RoundedFactorCheckpointData.panel11Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix28_eq :
    P2RoundedFactorCheckpointData.panel11Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk7.1

theorem panel11Prefix29_eq :
    P2RoundedFactorCheckpointData.panel11Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk7.2.1

theorem panel11Prefix30_eq :
    P2RoundedFactorCheckpointData.panel11Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk7.2.2.1

theorem panel11Prefix31_eq :
    P2RoundedFactorCheckpointData.panel11Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk7.2.2.2

end RHP2Bridge
