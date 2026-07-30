import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk7 :
    P2RoundedFactorCheckpointData.panel28Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix28_eq :
    P2RoundedFactorCheckpointData.panel28Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk7.1

theorem panel28Prefix29_eq :
    P2RoundedFactorCheckpointData.panel28Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk7.2.1

theorem panel28Prefix30_eq :
    P2RoundedFactorCheckpointData.panel28Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk7.2.2.1

theorem panel28Prefix31_eq :
    P2RoundedFactorCheckpointData.panel28Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk7.2.2.2

end RHP2Bridge
