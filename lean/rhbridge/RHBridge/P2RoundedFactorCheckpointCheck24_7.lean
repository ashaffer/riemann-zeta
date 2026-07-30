import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk7 :
    P2RoundedFactorCheckpointData.panel24Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix28_eq :
    P2RoundedFactorCheckpointData.panel24Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk7.1

theorem panel24Prefix29_eq :
    P2RoundedFactorCheckpointData.panel24Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk7.2.1

theorem panel24Prefix30_eq :
    P2RoundedFactorCheckpointData.panel24Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk7.2.2.1

theorem panel24Prefix31_eq :
    P2RoundedFactorCheckpointData.panel24Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk7.2.2.2

end RHP2Bridge
