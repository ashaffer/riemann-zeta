import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk4 :
    P2RoundedFactorCheckpointData.panel28Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix16_eq :
    P2RoundedFactorCheckpointData.panel28Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk4.1

theorem panel28Prefix17_eq :
    P2RoundedFactorCheckpointData.panel28Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk4.2.1

theorem panel28Prefix18_eq :
    P2RoundedFactorCheckpointData.panel28Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk4.2.2.1

theorem panel28Prefix19_eq :
    P2RoundedFactorCheckpointData.panel28Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk4.2.2.2

end RHP2Bridge
