import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk7 :
    P2RoundedFactorCheckpointData.panel21Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix28_eq :
    P2RoundedFactorCheckpointData.panel21Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk7.1

theorem panel21Prefix29_eq :
    P2RoundedFactorCheckpointData.panel21Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk7.2.1

theorem panel21Prefix30_eq :
    P2RoundedFactorCheckpointData.panel21Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk7.2.2.1

theorem panel21Prefix31_eq :
    P2RoundedFactorCheckpointData.panel21Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk7.2.2.2

end RHP2Bridge
