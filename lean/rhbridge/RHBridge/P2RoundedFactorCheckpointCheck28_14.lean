import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk14 :
    P2RoundedFactorCheckpointData.panel28Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix56_eq :
    P2RoundedFactorCheckpointData.panel28Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk14.1

theorem panel28Prefix57_eq :
    P2RoundedFactorCheckpointData.panel28Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk14.2.1

theorem panel28Prefix58_eq :
    P2RoundedFactorCheckpointData.panel28Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk14.2.2.1

theorem panel28Prefix59_eq :
    P2RoundedFactorCheckpointData.panel28Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk14.2.2.2

end RHP2Bridge
