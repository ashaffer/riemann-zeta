import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk7 :
    P2RoundedFactorCheckpointData.panel22Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix28_eq :
    P2RoundedFactorCheckpointData.panel22Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk7.1

theorem panel22Prefix29_eq :
    P2RoundedFactorCheckpointData.panel22Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk7.2.1

theorem panel22Prefix30_eq :
    P2RoundedFactorCheckpointData.panel22Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk7.2.2.1

theorem panel22Prefix31_eq :
    P2RoundedFactorCheckpointData.panel22Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk7.2.2.2

end RHP2Bridge
